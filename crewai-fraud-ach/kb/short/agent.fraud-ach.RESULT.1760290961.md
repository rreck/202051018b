```json
{
  "id": "3f85e4731cde234e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290961,
  "host_pid": "9e6742732c60:1",
  "hash": "8aef2a5eeaadeb4579e70e8895ddc04a488f872fc585ada89d26c4d562c68045",
  "cid": "QmV18aef2a5eeaadeb4579e70e8895ddc04a488f872f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290961,
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
      "evaluated_at": 1760290961
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
  "sig": "abf704c48178ff7c7e7dd427b31000a3423ded351d64f488e6254bc501054800"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 51874424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}