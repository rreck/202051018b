```json
{
  "id": "e10ef44eb80a3d35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293870,
  "host_pid": "9e6742732c60:1",
  "hash": "3259eed0fdac31d5137609d7c41ca3e04befee3d25276de2f28ac35f67fa23da",
  "cid": "QmV13259eed0fdac31d5137609d7c41ca3e04befee3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293870,
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
      "evaluated_at": 1760293870
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
  "sig": "0d407f50bea16ff93ea68dc7dc27750edb523382d098cbc9c758b40c1a10d2c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591886558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 71334069, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '37bcf4c9c4817870'}}}