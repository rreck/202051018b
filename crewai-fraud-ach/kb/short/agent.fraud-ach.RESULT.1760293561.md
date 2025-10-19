```json
{
  "id": "602df78810b5a40d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293561,
  "host_pid": "9e6742732c60:1",
  "hash": "0a2929fec171dd8f4bbc6d483805304749e217fb9a8249b65fb924230eaf9fbc",
  "cid": "QmV10a2929fec171dd8f4bbc6d483805304749e217fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293561,
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
      "evaluated_at": 1760293561
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
  "sig": "99330e57bb75e9fe01bb5509fdaf8e541932bc5b0c6b44ce2c995d816f616c49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464554990
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 60357973, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'ab9afd20a22fc7b8'}}}