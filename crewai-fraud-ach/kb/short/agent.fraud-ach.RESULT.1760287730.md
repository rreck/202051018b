```json
{
  "id": "24133df6adc2ac6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287730,
  "host_pid": "9e6742732c60:1",
  "hash": "b5c2dd6f9c4c580538a2a3acc892c7d8723e16343d86f6ba0cf2e2f81d9f274d",
  "cid": "QmV1b5c2dd6f9c4c580538a2a3acc892c7d8723e1634",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287730,
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
      "evaluated_at": 1760287730
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
  "sig": "85bd210d67832277d0bc4f6bc98fc53e18571ec3a9b1b9f3b0078b3b185ff808"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 121000240022849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 23341640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285765, 'matching_hash': 'fbe681be7d902297'}}}