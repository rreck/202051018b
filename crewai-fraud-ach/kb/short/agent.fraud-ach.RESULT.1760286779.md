```json
{
  "id": "8d759532a8801446",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286779,
  "host_pid": "9e6742732c60:1",
  "hash": "427f463273cf6d5b84e8518b021719bf419605e99a4ede6bea0e8e84896aede1",
  "cid": "QmV1427f463273cf6d5b84e8518b021719bf419605e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286779,
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
      "evaluated_at": 1760286779
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
  "sig": "d5082200a7e420a94692ebf6e056f51fd6a5b442cbb47505a5da857705eddf67"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034128514
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285763, 'matching_hash': '342851cb36b9daae'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285763, 'matching_hash': 'b939c4c4097f2f1f'}}}