```json
{
  "id": "15c09f89418dfe59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292360,
  "host_pid": "9e6742732c60:1",
  "hash": "92a3130fffbfcddf1f24b72f15ed72646ba757d925fb4e912272673077b699a7",
  "cid": "QmV192a3130fffbfcddf1f24b72f15ed72646ba757d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292360,
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
      "evaluated_at": 1760292360
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
  "sig": "fac7833262b795eaf49aee4f6f2897835d741df7e0ff51540416af326385c3e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242331672
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 22678376, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '532e279550beef55'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '361190711', 'validation_error': 'Invalid routing number checksum'}}}