```json
{
  "id": "7466ed131c32309f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291075,
  "host_pid": "9e6742732c60:1",
  "hash": "2329fc83246d973e43484502968cc5d6d051ba717009d3c7ce1d3ea32a21c614",
  "cid": "QmV12329fc83246d973e43484502968cc5d6d051ba71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291075,
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
      "evaluated_at": 1760291075
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
  "sig": "8e347344d964be98f26f6d769e9f6b50537caa381ae9b7fb3e53223618430ebf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593456245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 79974318, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285764, 'matching_hash': '5bbbd28055422217'}}}