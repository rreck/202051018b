```json
{
  "id": "04ffbfd9e576a4af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288190,
  "host_pid": "9e6742732c60:1",
  "hash": "c18bc65093c520a11f45629dd2a64e289bc72d1293a94a9d15e468d96864f18a",
  "cid": "QmV1c18bc65093c520a11f45629dd2a64e289bc72d12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288190,
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
      "evaluated_at": 1760288190
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
  "sig": "8be35c1325d9a21725efea40fb9a0be47515db6b9410d9215a49e512f06a927f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 27051080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}