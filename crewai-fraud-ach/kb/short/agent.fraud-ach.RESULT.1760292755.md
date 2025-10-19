```json
{
  "id": "62e5bc9194e7c45a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292755,
  "host_pid": "9e6742732c60:1",
  "hash": "8d4985f1a2dbe48053b298e70253b7a3c00a610db2d2231789e22e8b3adf04cb",
  "cid": "QmV18d4985f1a2dbe48053b298e70253b7a3c00a610d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292755,
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
      "evaluated_at": 1760292755
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
  "sig": "688e86bdf6ef971c2cbf32d1134c762261a864b49f6939e6464d5b73b1b4d854"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 77716452, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': 'a46c33998c9a26e1'}}}