```json
{
  "id": "c384f3a4dbaa1578",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294884,
  "host_pid": "9e6742732c60:1",
  "hash": "fe7ac38a35793ec3e8216e269b50eb979596e717f00ec493724e89c2433c2170",
  "cid": "QmV1fe7ac38a35793ec3e8216e269b50eb979596e717",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294884,
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
      "evaluated_at": 1760294884
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
  "sig": "18ff8908e29b95ce7e665a859e304602d3dc22b430d719bede14abaf7c43709e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029769834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 94600530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': '4022d05a51a758f8'}}}