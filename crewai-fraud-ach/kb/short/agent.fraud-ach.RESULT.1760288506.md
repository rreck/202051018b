```json
{
  "id": "2d9153254d9177be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288506,
  "host_pid": "9e6742732c60:1",
  "hash": "867e81cd87149b913f02d32b69bcf7079b4e8924b7c1a579cbe6601fbfb0a80b",
  "cid": "QmV1867e81cd87149b913f02d32b69bcf7079b4e8924",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288506,
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
      "evaluated_at": 1760288506
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
  "sig": "ea95370747059e7fbf24d21678c0aa8b5a72bbceb21139554c5c04b80201378f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598206386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 29503105, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285765, 'matching_hash': '83614fe1c845b0af'}}}