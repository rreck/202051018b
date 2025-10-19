```json
{
  "id": "7252176ef0332efe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293175,
  "host_pid": "9e6742732c60:1",
  "hash": "491d0e52a0d4d7f005d856ea805490748caab9f4842229bbc28d302233d4a726",
  "cid": "QmV1491d0e52a0d4d7f005d856ea805490748caab9f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293175,
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
      "evaluated_at": 1760293175
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
  "sig": "2be3743dad13977360b2037094e60f753a7c26db0c98bb40bf25787bdd6752ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029068175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 74352123, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': 'd04fb7e5778b56f7'}}}maly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8435125}}}