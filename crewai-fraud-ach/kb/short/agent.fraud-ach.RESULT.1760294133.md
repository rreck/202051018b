```json
{
  "id": "46c586e71d475769",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294133,
  "host_pid": "9e6742732c60:1",
  "hash": "37a1e7b5bb00f386e564dd856cf227eb6ddeff2605d72ea7f299ff095f6971a3",
  "cid": "QmV137a1e7b5bb00f386e564dd856cf227eb6ddeff26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294133,
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
      "evaluated_at": 1760294133
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
  "sig": "8d4859d17464195d53cb717c7c07a266cdbd3bebaed3ea77d2b32d109ca2b59e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245017605
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 109138832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}