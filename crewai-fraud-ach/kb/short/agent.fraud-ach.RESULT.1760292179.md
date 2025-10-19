```json
{
  "id": "844a2ea268f16a5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292179,
  "host_pid": "9e6742732c60:1",
  "hash": "15e63bb034b6bb8b7a98825202558a642fa871dc80b81028a09a401bb1acba0e",
  "cid": "QmV115e63bb034b6bb8b7a98825202558a642fa871dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292179,
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
      "evaluated_at": 1760292179
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
  "sig": "35653e01b62820c5651d272ba8d756a4a111b660efdf78712b10a00795a5a209"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022959454
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 28879488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'd9e1e1b77e5bc9b7'}}}