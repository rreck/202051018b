```json
{
  "id": "ab5b24a365a654e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287849,
  "host_pid": "9e6742732c60:1",
  "hash": "0637791117368bbed3529d33271abf8c962c3bed493414323754f7ae31fcdfcb",
  "cid": "QmV10637791117368bbed3529d33271abf8c962c3bed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287849,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760287849
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "77aabdaa61c5d1847513e6b90d6c86da8b07b08f9ec157063f8d8dbc1ebbba67"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 044000039498282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 36869908, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285765, 'matching_hash': 'dad018b424b66512'}}}