```json
{
  "id": "6557f231efd4e480",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290638,
  "host_pid": "9e6742732c60:1",
  "hash": "f4271ec6da5a4ebb059a82417e07c77a6d27e34591694f710ffb2578ff69e5b7",
  "cid": "QmV1f4271ec6da5a4ebb059a82417e07c77a6d27e345",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290638,
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
      "evaluated_at": 1760290638
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
  "sig": "5de1136fa83f2f11cd9a61cbbf4d3a3a5f1153f532ddd5fbd7970531012054ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153539871
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 38750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285765, 'matching_hash': '6120bfc166994b37'}}}