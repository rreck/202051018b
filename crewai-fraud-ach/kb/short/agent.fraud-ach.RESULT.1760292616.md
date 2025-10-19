```json
{
  "id": "baa809b1fe5db2e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292616,
  "host_pid": "9e6742732c60:1",
  "hash": "6a7f1328868a58c2a2f7475e9c3ca0e49168b09d3b11821fb49bab370370d3a2",
  "cid": "QmV16a7f1328868a58c2a2f7475e9c3ca0e49168b09d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292616,
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
      "evaluated_at": 1760292616
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
  "sig": "7c4fd205c5b4bdf96041f965dba3ab78b21cab9a40d208f909d794810a8160c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 16941687, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}