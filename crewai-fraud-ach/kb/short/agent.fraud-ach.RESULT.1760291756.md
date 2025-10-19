```json
{
  "id": "1ca789be4d454b9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291756,
  "host_pid": "9e6742732c60:1",
  "hash": "1a5f3e26b702541abb2cf5a9e5fae4c37af9081ba9358fe3fc0fdca3345baa81",
  "cid": "QmV11a5f3e26b702541abb2cf5a9e5fae4c37af9081b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291756,
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
      "evaluated_at": 1760291756
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
  "sig": "37edd66cbfe0bfce97c5237b180b1ac6a5a441bf0a6280715b6a31b443728c23"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242987850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 21299278, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285764, 'matching_hash': 'ac2312cc15fe4af9'}}}