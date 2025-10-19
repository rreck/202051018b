```json
{
  "id": "af6e6b9dd4e07528",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292993,
  "host_pid": "9e6742732c60:1",
  "hash": "032326268a92d9299be2ff449aecdc14edd5055a2c0ff57ffe0567e4aa28a15d",
  "cid": "QmV1032326268a92d9299be2ff449aecdc14edd5055a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292993,
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
      "evaluated_at": 1760292993
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
  "sig": "e0969e067a12133cecade8dd7b2da69dabc41a295180a83687459dba966085f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468256911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 37938098, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': 'b0ec3a54cf0504a9'}}}