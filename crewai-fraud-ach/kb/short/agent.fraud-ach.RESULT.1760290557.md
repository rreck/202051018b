```json
{
  "id": "5ed1049208758a71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290557,
  "host_pid": "9e6742732c60:1",
  "hash": "e1f0f32311cb2a84d12f6229b4902aaa0015e2f91d0bf62814ba9b6532d3fdc9",
  "cid": "QmV1e1f0f32311cb2a84d12f6229b4902aaa0015e2f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290557,
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
      "evaluated_at": 1760290557
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
  "sig": "0056cc9836a3b426899ef0cef916f31e5c414cdc394c9d9e7a8cf9df652a5e52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025325708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 49304709, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285765, 'matching_hash': '23dd43a9dda0a05d'}}}