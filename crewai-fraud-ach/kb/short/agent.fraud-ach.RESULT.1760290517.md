```json
{
  "id": "41595545a1880776",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290517,
  "host_pid": "9e6742732c60:1",
  "hash": "0c0c0c464c1f7c00b0a88ec654e31c5874f20b9e0a1e085f8b7e6e68e7759ce9",
  "cid": "QmV10c0c0c464c1f7c00b0a88ec654e31c5874f20b9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290517,
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
      "evaluated_at": 1760290517
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
  "sig": "7dc4eb38a517d0c9319be27e3eb0abd9b19497837b5f86ee43c4e21db606815b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034581430
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 61637976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285764, 'matching_hash': '1e0cfdc13a2b6c27'}}}