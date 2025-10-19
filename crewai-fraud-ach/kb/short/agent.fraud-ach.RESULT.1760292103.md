```json
{
  "id": "90f456bcdda956d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292103,
  "host_pid": "9e6742732c60:1",
  "hash": "2f286cc94cc3ec2ceda1d736d97c1063fc3d1b333c4d87d6d5b5ffa2a4033802",
  "cid": "QmV12f286cc94cc3ec2ceda1d736d97c1063fc3d1b33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292103,
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
      "evaluated_at": 1760292103
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
  "sig": "7fd95a83c76cbaebc1bf259086a856d843a49200f5a3189abc0f8c8ff0723926"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279768309
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 266, 'threshold': 50, 'total_amount': 22175090, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 265, 'first_seen': 1760284979, 'matching_hash': '8798983dc5a8227d'}}}