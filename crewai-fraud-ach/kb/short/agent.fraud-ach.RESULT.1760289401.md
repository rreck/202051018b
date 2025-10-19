```json
{
  "id": "0f83be19b12abe15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289401,
  "host_pid": "9e6742732c60:1",
  "hash": "329e9ba75e1e3ea3353013c258d3586edf04b708ef0fdc394d9ecfa578e0afec",
  "cid": "QmV1329e9ba75e1e3ea3353013c258d3586edf04b708",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289401,
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
      "evaluated_at": 1760289401
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
  "sig": "7c2073af78df6ebbe2cc2cccef5530ec0330db0ed4feb454067484dafe49e82f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023367694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 51166190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '23afc27b7b9a7115'}}}