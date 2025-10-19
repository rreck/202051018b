```json
{
  "id": "2c3d391aeb1165d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290056,
  "host_pid": "9e6742732c60:1",
  "hash": "b53cfd801b325f0d7a9279938ea56d3916b262432812b3bc2dd4b9c19685f3de",
  "cid": "QmV1b53cfd801b325f0d7a9279938ea56d3916b26243",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290056,
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
      "evaluated_at": 1760290056
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
  "sig": "a1047e9a13e37dc745609d14882382879c324820d386a8e1bad398a87e13811b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021005824
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': '58a86144ce85b895'}}}