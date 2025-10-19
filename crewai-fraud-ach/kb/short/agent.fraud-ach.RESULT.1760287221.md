```json
{
  "id": "d783a8676ca6d556",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287221,
  "host_pid": "9e6742732c60:1",
  "hash": "60655055c9689bf336bdf6072b24c6b7843f15d153d1c1b0f0fe089813d6bf37",
  "cid": "QmV160655055c9689bf336bdf6072b24c6b7843f15d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287221,
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
      "evaluated_at": 1760287221
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "ec9cef835b26e35b3590fb7068ef74390416c7c5efb231f8760c92b40e8af677"
}
```

Fraud detected: duplicate_transaction (score: 69)
Transaction: 026009597164999
Details: {'velocity': {'fraud_detected': True, 'risk_score': 54, 'details': {'transaction_count': 52, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285765, 'matching_hash': 'b2fd55917469a01e'}}}