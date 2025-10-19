```json
{
  "id": "4d5bde8929704463",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294877,
  "host_pid": "9e6742732c60:1",
  "hash": "62c7d2202f57b74ea3fe3c50873720ee48d813308830665376c48d8a9985d782",
  "cid": "QmV162c7d2202f57b74ea3fe3c50873720ee48d81330",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294877,
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
      "evaluated_at": 1760294877
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
  "sig": "5a7ef5cc75555297d5e95383d98a9397f654f732eb6dd23218ddd68372764276"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024591055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 113993202, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '8a72f4eb6bbba5d7'}}}