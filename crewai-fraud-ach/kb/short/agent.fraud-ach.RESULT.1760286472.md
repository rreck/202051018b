```json
{
  "id": "5fbc7685175002f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286472,
  "host_pid": "9e6742732c60:1",
  "hash": "51858d13c6eff95809865880c1705d23ccff32f6141dd0d2d3d2640edbc17e78",
  "cid": "QmV151858d13c6eff95809865880c1705d23ccff32f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286472,
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
      "evaluated_at": 1760286472
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
  "sig": "4f7206a9f51d8edf97e3d10b40888c96ba11bd72dd680a9f545bbea5c9060f90"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009597164999
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285765, 'matching_hash': 'b2fd55917469a01e'}}}