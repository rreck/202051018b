```json
{
  "id": "e24e2cbcb18b4b0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288542,
  "host_pid": "9e6742732c60:1",
  "hash": "f4fa2b226174d0b7ed74d3cb18cf4902229ef0a2e4d643d008766d615cc62ab9",
  "cid": "QmV1f4fa2b226174d0b7ed74d3cb18cf4902229ef0a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288542,
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
      "evaluated_at": 1760288542
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
  "sig": "af6e93c8519868405719ea283f829148510bb4dfd7149919963bc3b73e93d180"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 30551808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}