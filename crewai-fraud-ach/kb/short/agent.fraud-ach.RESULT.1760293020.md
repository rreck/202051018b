```json
{
  "id": "2bf83bc94f32fcf2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293020,
  "host_pid": "9e6742732c60:1",
  "hash": "ee5406f4b567ea16d96d7a7fcc08c4464bd080e44d3bf0b34b5ce0f46f768674",
  "cid": "QmV1ee5406f4b567ea16d96d7a7fcc08c4464bd080e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293020,
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
      "evaluated_at": 1760293020
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
  "sig": "58d96bbc0a4b263bff261894f7326579adde8d0aa3ee6bf3e8e82a45e1ceda28"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469776996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 34503000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '22919e1176d7109e'}}}