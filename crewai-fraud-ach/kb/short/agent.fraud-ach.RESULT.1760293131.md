```json
{
  "id": "1cb3e7acf599f73f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293131,
  "host_pid": "9e6742732c60:1",
  "hash": "30ff3546b4faf1e80ade39fac24fdaf34808a942e464a40b07ed0b6916170f03",
  "cid": "QmV130ff3546b4faf1e80ade39fac24fdaf34808a942",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293131,
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
      "evaluated_at": 1760293131
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
  "sig": "936f60b481c6bd47eb1eb0f9d35f76ac3136ae0dcb5da37766cbc2805a5f521e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595571766
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 104214748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '7b9b43f48a0de4d3'}}}