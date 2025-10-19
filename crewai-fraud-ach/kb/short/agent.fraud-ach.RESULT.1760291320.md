```json
{
  "id": "d23f75685439b00a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291320,
  "host_pid": "9e6742732c60:1",
  "hash": "d7455ae79509c494cf7011175bf66837069c3704830bf3456d7b7fece794a68f",
  "cid": "QmV1d7455ae79509c494cf7011175bf66837069c3704",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291320,
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
      "evaluated_at": 1760291320
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
  "sig": "af6fb9eecbc2eddf26b964113f4dce43264fbcc8797ab07793b58acdf512de90"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022844283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 248, 'threshold': 50, 'total_amount': 46717000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 247, 'first_seen': 1760284979, 'matching_hash': '9c963f39e9fb9122'}}}