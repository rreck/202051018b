```json
{
  "id": "c218540eee08c160",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290348,
  "host_pid": "9e6742732c60:1",
  "hash": "7e99f47cbdc21407e4478845ca6439e3e1b0f3b3447bcac01fac31f6bf935cbf",
  "cid": "QmV17e99f47cbdc21407e4478845ca6439e3e1b0f3b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290348,
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
      "evaluated_at": 1760290348
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "0b1af0b8d268116780925d92736792c80f2e2ca8cb73ef684acb9187c995f300"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 614505621863127
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 41085096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285764, 'matching_hash': '8748c624c8dfcb5e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '614505622', 'validation_error': 'Invalid routing number checksum'}}}