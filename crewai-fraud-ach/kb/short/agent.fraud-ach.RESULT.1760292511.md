```json
{
  "id": "a117f4c0cd306048",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292511,
  "host_pid": "9e6742732c60:1",
  "hash": "1b1eb25189cc22d960646c20c5b0aecbfb266e628fdb9672bc922beb6050f33c",
  "cid": "QmV11b1eb25189cc22d960646c20c5b0aecbfb266e62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292511,
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
      "evaluated_at": 1760292511
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
  "sig": "7f37e79382f74186e83a300259fb3d3ba335e439c51b71760fc482ffa6f27ee1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153734827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 98195555, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': 'f575a9f929aab221'}}}