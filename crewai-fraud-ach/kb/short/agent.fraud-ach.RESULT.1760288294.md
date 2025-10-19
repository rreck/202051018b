```json
{
  "id": "4b4fd13ad5916f03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288294,
  "host_pid": "9e6742732c60:1",
  "hash": "e6dd2b47ecdebeef6f0aa31840c19af6feb6110a9618be26fa0dd2bd25e5f2a0",
  "cid": "QmV1e6dd2b47ecdebeef6f0aa31840c19af6feb6110a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288294,
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
      "evaluated_at": 1760288294
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
  "sig": "490e7464b908600e513a1ffbe1690e7aac408b1690865d7ce7a2d71ab662ea3a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599280040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 43323954, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': '3242f38050bfb93d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}