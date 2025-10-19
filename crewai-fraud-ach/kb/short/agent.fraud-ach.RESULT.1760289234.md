```json
{
  "id": "e3a20603c1eb7a4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289234,
  "host_pid": "9e6742732c60:1",
  "hash": "0e1bd2d45a9905e5a61dd8c867805aca44789323c6bd64d2d6778d23f9ae922e",
  "cid": "QmV10e1bd2d45a9905e5a61dd8c867805aca44789323",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289234,
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
      "evaluated_at": 1760289234
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
  "sig": "30296a55d57c6e813020d707b69c1b048fd2dc9798969a38df62d63b538e6085"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464170386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285764, 'matching_hash': 'cc3f2cd033134006'}}}