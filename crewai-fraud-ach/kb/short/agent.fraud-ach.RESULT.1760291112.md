```json
{
  "id": "adb40d56e3d5f848",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291112,
  "host_pid": "9e6742732c60:1",
  "hash": "fdcf56ed6b8edc5e48f8acb9f6f8706be5467cdddc19052845d0a31f9ab24b68",
  "cid": "QmV1fdcf56ed6b8edc5e48f8acb9f6f8706be5467cdd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291112,
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
      "evaluated_at": 1760291112
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
  "sig": "5be0f185c983df2bb62fa551d49087f7feb5351d3c5d2354862a39fe196e5528"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276148173
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 47210065, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': 'f15677eba424e05f'}}}