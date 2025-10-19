```json
{
  "id": "0c4ea745af6ec595",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290096,
  "host_pid": "9e6742732c60:1",
  "hash": "97da58eccd4f65e287bb381a0f9f2147d9fda8c32061f6f1f7020f28b3dfb751",
  "cid": "QmV197da58eccd4f65e287bb381a0f9f2147d9fda8c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290096,
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
      "evaluated_at": 1760290096
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
  "sig": "250b0fb7c65d9fc90c68ea4ee1a375e19525fd8aa1a9a8393706b96051a9f094"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027918613
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 16044672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285764, 'matching_hash': 'c11d1385920c0a28'}}}