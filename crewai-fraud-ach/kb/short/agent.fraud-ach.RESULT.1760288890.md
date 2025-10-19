```json
{
  "id": "dec88bf68aa59f0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288890,
  "host_pid": "9e6742732c60:1",
  "hash": "16b5d5d159bc9b236a1647185a1f15f0c2011cbcce550030cd65cbf0248a09a9",
  "cid": "QmV116b5d5d159bc9b236a1647185a1f15f0c2011cbc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288890,
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
      "evaluated_at": 1760288890
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
  "sig": "37514196ee620dea162542e92867d370bd5e5aab7d411bb3259c98d0944cdfd8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270359022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 23909471, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'b3fe4d9c14539f22'}}}