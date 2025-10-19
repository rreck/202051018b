```json
{
  "id": "d0bd4d533bbe0a10",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294810,
  "host_pid": "9e6742732c60:1",
  "hash": "173339bd796d54eaf0a51d09bbeacee208e7bdcabd05b10b5010b33cb2bf45b9",
  "cid": "QmV1173339bd796d54eaf0a51d09bbeacee208e7bdca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294810,
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
      "evaluated_at": 1760294810
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
  "sig": "b8c3c7121f6a8155c74457d752ba8ac1b4745a29cbf29c1f14a1392500d836f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596329202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 42625100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'fa5bd443d3b1bd8d'}}}maly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.69, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7209366}}}