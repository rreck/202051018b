```json
{
  "id": "5f8eabd62605a0b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294189,
  "host_pid": "9e6742732c60:1",
  "hash": "81b58a15f47894b3704293162c0e5a202b82eed9e77fa6b1e844cd1571ee8125",
  "cid": "QmV181b58a15f47894b3704293162c0e5a202b82eed9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294189,
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
      "evaluated_at": 1760294189
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
  "sig": "6f4e5e2170fdd63bec9de9da3744931adf812644fc371a74a8cbf771e55e73f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 55880390, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '7b717df8c1c9c887'}}}