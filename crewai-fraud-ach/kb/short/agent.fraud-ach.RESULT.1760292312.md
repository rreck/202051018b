```json
{
  "id": "68027ac76f169e7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292312,
  "host_pid": "9e6742732c60:1",
  "hash": "8d5478a0b1353c8bf9f0673d4e9b336391daa78e0596bff169abf2fe32f249ba",
  "cid": "QmV18d5478a0b1353c8bf9f0673d4e9b336391daa78e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292312,
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
      "evaluated_at": 1760292312
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
  "sig": "5b6d35778441c8e5aa70d5f069b758de2ddc334c51da086ec6a631b1a6691b9d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150868994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 80811315, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '612406b6271445a9'}}}maly': {'fraud_detected': True, 'risk_score': 85, 'details': {'zscore': 4.56, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8725948}}}