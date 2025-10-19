```json
{
  "id": "34d69bbf82d4abf1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289545,
  "host_pid": "9e6742732c60:1",
  "hash": "d9931e73c792e80a9f26a194cac772d2076bf993b060046fcc9a2a9126cfe07a",
  "cid": "QmV1d9931e73c792e80a9f26a194cac772d2076bf993",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289545,
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
      "evaluated_at": 1760289545
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
  "sig": "048121cf0a2446707862548223cd9e3b8f641486915d744021ecc0b1d3ac12bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241083307
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 11511234, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '06ddfe971a6a4d24'}}}