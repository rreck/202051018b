```json
{
  "id": "f8330ee75f54f211",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291163,
  "host_pid": "9e6742732c60:1",
  "hash": "d0480bc2d6888891a238d2200bd1396bfa5c65de7624bd74f51f81cc101549c1",
  "cid": "QmV1d0480bc2d6888891a238d2200bd1396bfa5c65de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291163,
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
      "evaluated_at": 1760291163
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
  "sig": "4dca11eea2cc7fb6ca22733d734b4398e627fe369865eb5358ad23dca7f4099a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597164999
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 30107280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285765, 'matching_hash': 'b2fd55917469a01e'}}}