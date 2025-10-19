```json
{
  "id": "fcdce248401ebcb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290942,
  "host_pid": "9e6742732c60:1",
  "hash": "98e126a4ed857b3dd2cdf09d937e04af5022b67129209f1b1e860f61298e63d6",
  "cid": "QmV198e126a4ed857b3dd2cdf09d937e04af5022b671",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290942,
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
      "evaluated_at": 1760290942
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
  "sig": "c56a424a3d0d464a7276e0f34958c05ad420ff0dbdd788b1f704e0c0899a74fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461947560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 52689098, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285764, 'matching_hash': '1e39107ec95e1ca0'}}}