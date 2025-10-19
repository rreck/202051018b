```json
{
  "id": "0e87c573609d725b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293484,
  "host_pid": "9e6742732c60:1",
  "hash": "96892d2e5bacabbcd7ea44212b719718653cb21d2e8aa2ea2e246f4a65adf8ba",
  "cid": "QmV196892d2e5bacabbcd7ea44212b719718653cb21d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293484,
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
      "evaluated_at": 1760293484
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
  "sig": "fe52a1575b64ec199f1d6acb00035af74a3597262a91c0d5a64b7ea8b2f94a4d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 12510156, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}