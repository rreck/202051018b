```json
{
  "id": "38cf3a505c4bda80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285869,
  "host_pid": "9e6742732c60:1",
  "hash": "0c75938f8a909f26005f95b8f4520e753e65dd2d82f4fa6f3cf36071740c4f92",
  "cid": "QmV10c75938f8a909f26005f95b8f4520e753e65dd2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285869,
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
      "evaluated_at": 1760285869
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
  "sig": "4d516de458daa4e3e5db036972ae2511d60715dba7ead62de22977852e4f75c3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100279738088
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': '31a7269ac1c5c77d'}}}