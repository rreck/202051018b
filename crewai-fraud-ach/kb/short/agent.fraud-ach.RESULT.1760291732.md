```json
{
  "id": "3be58d06de727911",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291732,
  "host_pid": "9e6742732c60:1",
  "hash": "5cfa764d6c4747866797e279effe86f2b47cce5ed2b9365f707b121251d4eb62",
  "cid": "QmV15cfa764d6c4747866797e279effe86f2b47cce5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291732,
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
      "evaluated_at": 1760291732
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
  "sig": "27bdbff4e9e50c24b50fb7d30ba9e594fd0a8e32f8fe546acf887b995b4a5000"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 667325182164908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 29878576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '7f033df851d7a625'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '667325181', 'validation_error': 'Invalid routing number checksum'}}}