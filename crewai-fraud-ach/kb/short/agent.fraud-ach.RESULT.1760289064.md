```json
{
  "id": "47dd9e5087632369",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289064,
  "host_pid": "9e6742732c60:1",
  "hash": "5ad3165e021bb046fd836d2ae20bb096e33d307afcdf68615c62b3589e0a9e78",
  "cid": "QmV15ad3165e021bb046fd836d2ae20bb096e33d307a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289064,
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
      "evaluated_at": 1760289064
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
  "sig": "4b25936b581de0a20a085b81881527cddf169a1eebd1bb72a478f402ef97e210"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027918613
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 12744704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285764, 'matching_hash': 'c11d1385920c0a28'}}}