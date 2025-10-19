```json
{
  "id": "ae704a45b815c69e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293209,
  "host_pid": "9e6742732c60:1",
  "hash": "f007faa05027bcdefd31726d70147bf89d88c6154b1c3e75af80d9f716140d7c",
  "cid": "QmV1f007faa05027bcdefd31726d70147bf89d88c615",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293209,
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
      "evaluated_at": 1760293209
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
  "sig": "c1ae8a849e6a3cadca7d280b5f8ec21dbc890ebcfca83223b889ec9361a2fb73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591082294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 99394654, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': 'b890dc886075e9be'}}}