```json
{
  "id": "a022f74d06141a37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286980,
  "host_pid": "9e6742732c60:1",
  "hash": "8f0ef5f462e15355d93c09330139ab85c04747b07d7dd920606eacf082c6f826",
  "cid": "QmV18f0ef5f462e15355d93c09330139ab85c04747b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286980,
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
      "evaluated_at": 1760286980
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
  "sig": "42d61fe63ae4d04aae6c9b3969e98de41b6a314522c60056d74845e429c3750b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105155862167
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': '207d73478b089b6e'}}}, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': 'd907a2a28cc997b7'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}