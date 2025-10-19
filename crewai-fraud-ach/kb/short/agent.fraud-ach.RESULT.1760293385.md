```json
{
  "id": "a432252ad55c7aea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293385,
  "host_pid": "9e6742732c60:1",
  "hash": "708ab36f9cc89c19dd0fe2618b3e50e2b428186dd68bc83bdcf21f7816b653dc",
  "cid": "QmV1708ab36f9cc89c19dd0fe2618b3e50e2b428186d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293385,
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
      "evaluated_at": 1760293385
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
  "sig": "63951be5db7f8c5a6f1766cd920a54e7779fa6c5f1124ebd6ae6c4cd9f22db86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027918613
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 24692864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': 'c11d1385920c0a28'}}}