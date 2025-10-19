```json
{
  "id": "41d41e00371715e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292799,
  "host_pid": "9e6742732c60:1",
  "hash": "592a8f7def90b15cf559facc934c2c7500efe74181268c9b06fa39644797a2be",
  "cid": "QmV1592a8f7def90b15cf559facc934c2c7500efe741",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292799,
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
      "evaluated_at": 1760292799
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
  "sig": "2b5b0c087c5fa5387b5244afd6c8ca2990270e6a33629612c95de168847ebbed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598219019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 23411615, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': '253a69ee76b5426a'}}}