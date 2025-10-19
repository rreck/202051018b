```json
{
  "id": "6bef58b080c96287",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286073,
  "host_pid": "9e6742732c60:1",
  "hash": "7471098222c94fe1b0cd7747549126a2a741e696735f242b942abe158b582d01",
  "cid": "QmV17471098222c94fe1b0cd7747549126a2a741e696",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286073,
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
      "evaluated_at": 1760286073
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
  "sig": "16f0887df0b03054058e1a44e646e64d6afd60bbd194869c80ad996eed6df198"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000244341450
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285765, 'matching_hash': '31d93fdc369ae63d'}}}