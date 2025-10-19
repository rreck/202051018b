```json
{
  "id": "48a91bda229ab460",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287438,
  "host_pid": "9e6742732c60:1",
  "hash": "f151e1db1f349dddb455c1114991a3f4a908cee6adf749cd83cef2831a5829cc",
  "cid": "QmV1f151e1db1f349dddb455c1114991a3f4a908cee6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287438,
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
      "evaluated_at": 1760287438
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "f2ef52ef03c0b7c7ba1e2bd9477c7cf7ec6e48c2b7109e8006146e7f9059e2b4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000021395098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 21649560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285765, 'matching_hash': '9c6ceec1730a6176'}}}